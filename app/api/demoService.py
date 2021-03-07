import datetime
import os
import ast
import logging
import json
import concurrent.futures
from google.cloud import bigtable
from google.cloud.bigtable import column_family
from google.cloud.bigtable import row_filters
from google.cloud.bigtable.row_set import RowSet
from flask_restful import Resource, reqparse
from dotenv import load_dotenv, find_dotenv

LOGLEVEL = os.environ.get('LOGLEVEL', 'WARNING').upper()
logger = logging.getLogger(__name__)
logging.basicConfig(format="%(name)s %(process)d/%(threadName)s:%(message)s", level=LOGLEVEL)


# When running locally set the below env vars in a .env file (same level as main.py) with GOOGLE_APPLICATION_CREDENTIALS for bigtable
# ex: GOOGLE_APPLICATION_CREDENTIALS = "credentials/credential.json"   (credentials folder same level as main.py)
load_dotenv(find_dotenv())
   

project_name = os.environ.get('GCP_PROJECT')
instance_name = os.environ.get('BT_INSTANCE')
bt_mapping_dict = ast.literal_eval(os.environ.get('BT_MAPPING'))
bt_table_name = os.environ.get('BT_TABLE_NAME')
row_keys = os.environ.get('BT_ROW_KEYS').split(",")

client = bigtable.Client(project=project_name)
instance = client.instance(instance_name)


class DemoHelloWorld(Resource):
    def get (self):
        return json.dumps({'message':'Hi !!'}), 200, {'ContentType':'application/json'} 

class DemoBigTableGet(Resource):
    def get (self):
        bt_array = []
        try:
            
            table = instance.table(bt_table_name)
            row_set = RowSet()

            for row_key in row_keys:
                row_set.add_row_key(row_key)

            colFilters = []
            for name, bt_name in bt_mapping_dict.items():
                colFilters.append(row_filters.ColumnQualifierRegexFilter(bt_name))

            print("before read_rows...")
            rows = table.read_rows(row_set=row_set, filter_=row_filters.RowFilterChain(filters=[row_filters.CellsColumnLimitFilter(1), row_filters.RowFilterUnion(filters=colFilters)]),retry=bigtable.table.DEFAULT_RETRY_READ_ROWS.with_deadline(60.0))
            print("after read_rows...")

            for row in rows:
                print("Reading data for {}:".format(row.row_key.decode('utf-8')))
                for cf, cols in sorted(row.cells.items()):
                    bt_dict = {}
                    bt_dict['id'] = row.row_key.decode('utf-8')
                    key = None
                    # using BT mapping to return  data
                    for col, cells in sorted(cols.items()):
                        for cell in cells:
                            for name, bt_name in bt_mapping_dict.items():
                                if col.decode('utf-8') == bt_name:
                                    key = name
                                    break
                            if key is not None:
                                bt_dict[key] = cell.value.decode('utf-8')
                    bt_array.append(bt_dict)
        except BaseException as error:
            logging.error('An exception occurred - DemoBigTableGet::get(): {}'.format(error))

        print(bt_array)

        return json.dumps(bt_array), 200, {'ContentType':'application/json'} 

class DemoServiceReadiness(Resource):
    def get(self):
        return json.dumps({'Ready':True}), 200, {'ContentType':'application/json'} 

    def post(self):
        return json.dumps({'Ready':True}), 200, {'ContentType':'application/json'} 

class DemoServiceLiveness(Resource):
    def get(self):
        return json.dumps({'Alive':True}), 200, {'ContentType':'application/json'} 

    def post(self):
        return json.dumps({'Alive':True}), 200, {'ContentType':'application/json'} 

class DemoServiceHealth(Resource):
    def get(self):
        return json.dumps({'Healthy':True}), 200, {'ContentType':'application/json'} 

    def post(self):
        return json.dumps({'Healthy':True}), 200, {'ContentType':'application/json'} 


#DemoBigTableGet().get()