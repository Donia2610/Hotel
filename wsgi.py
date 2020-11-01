from app import create_app # From the folder app import the variable app
import config


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
