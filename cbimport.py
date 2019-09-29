from couchbase.cluster import Cluster
from couchbase.cluster import PasswordAuthenticator

import uuid
import json

cluster = Cluster('couchbase://localhost')
authenticator = PasswordAuthenticator('username', 'password')
cluster.authenticate(authenticator)
cb = cluster.open_bucket('bucket_name')

with open("/path/to/json/from/cb.json") as infile:
	data_list = json.loads(infile.read())
	# :todo: bulk insert
	for row in data_list:
		cb.insert(str(uuid.uuid4()), row)
