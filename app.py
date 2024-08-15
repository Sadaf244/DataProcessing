from flask import Flask, jsonify
import random
app=Flask(__name__)
processed_data_store={}
mock_data={
     "shop_1":{"name":"shopify store1", "sales": [8900,2200,300]},
     "shop_2":{"name":"shopify store2", "sales": [150,250,350]},
     "shop_3":{"name":"shopify store3", "sales": [50,70,120]},
     "shop_4":{"name":"shopify store4", "sales": [1000,200,70]},
     "shop_5":{"name":"shopify store5", "sales": [1930,340,280]},
     "shop_6":{"name":"shopify store6", "sales": [290,800,450]},
     "shop_7":{"name":"shopify store7", "sales": [1065,3780,8760]},
     "shop_8":{"name":"shopify store8", "sales": [876,457,390]},
     "shop_9":{"name":"shopify store9", "sales": [170,550,309]},
     "shop_10":{"name":"shopify store10", "sales": [10,290,30]},
}


@app.route('/fetch-data/<shop_id>', methods=['GET'])
def fetch_data(shop_id):
    if shop_id not in mock_data:
        return jsonify({"message": "No data available"}), 200

    fetched_data = mock_data[shop_id]
    processed_data = {
     "name": fetched_data["name"].upper(),
     "total_sales": sum(fetched_data["sales"]),
    }
    processed_data_store[shop_id] = processed_data

    return jsonify({"message": "Data fetched and processed", "data" : processed_data}), 200


@app.route('/get_processed-data', methods=['GET'])
def get_processed_data():
    if not processed_data_store:
        return jsonify({"message" : "No data available"}), 200

    return jsonify(processed_data_store), 200


if __name__ == '__main__':
    app.run(debug=True)
