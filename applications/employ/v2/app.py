from applications.employ.v2.routes import Routes

if __name__ == '__main__':
    routes = Routes()
    routes.configure_routes()
    routes.app.run(host='0.0.0.0', port=6000, debug=True)

