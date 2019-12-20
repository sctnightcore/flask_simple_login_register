from flask import url_for
def test_router_index(client):
	res = client.get(url_for('router.index'))
	assert res.status_code == 200
