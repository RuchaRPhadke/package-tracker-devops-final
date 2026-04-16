from flask import Flask, request, jsonify
import time

app = Flask(__name__)

def get_package(tracking_id):
    # Change status every 10 seconds
    current_time = int(time.time() / 10) % 4

    status_flow = [
        "Order Placed",
        "Shipped",
        "Out for Delivery",
        "Delivered"
    ]

    locations = [
        "Warehouse",
        "City Hub",
        "Near Destination",
        "Delivered Location"
    ]

    if tracking_id.startswith("PKG"):
        return {
            "tracking_id": tracking_id,
            "status": status_flow[current_time],
            "location": locations[current_time]
        }
    else:
        return {
            "tracking_id": tracking_id,
            "status": "Invalid ID",
            "location": "Unknown"
        }

@app.route("/track")
def track():
    tracking_id = request.args.get("id", "PKG1")
    result = get_package(tracking_id)
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)