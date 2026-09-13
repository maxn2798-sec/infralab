from fastapi import FastAPI

app = FastAPI(
    title="Infralab API",
    description="API for infrastructure management",
    version="0.1.0",
)

@app.get("/")
def root():
    return {
        "project": "Infralab",
        "status": "online",
        "version": "0.1.0"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

lista_servers = []

@app.get("/servers/count")
def get_servers_count():
    return {
         "count": 0
    }

@app.get("/servers")
def servers():
    return lista_servers
            
@app.get("/about")
def about():
    return{
        "name": "InfraLab",
        "author": "Max N",
        "purpose": "Infrastructure management"
    }

@app.get("/version")
def version():
    return {
        "version": "0.1.0"
    }