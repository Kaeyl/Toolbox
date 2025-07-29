import docker
from getpass import getpass
client = docker.from_env()


viewExistingContainers = client.containers.list(all=True)

def createContainer(inputUser, inputPassword, dbname, containerName, containerPort, client):
    # client = docker.from_env()
    try:
        container = client.containers.run(
            "postgres:15",
            name=containerName,
            environment={
                "POSTGRES_USER": inputUser,
                "POSTGRES_PASSWORD": inputPassword,
                "POSTGRES_DB": dbname
            },
            ports={"5432/tcp": int(containerPort)},
            detach=True  # Runs the container in the background
        )

        print(f"Container {container.name} created and running.")
    except docker.errors.APIError as e:
        print(f"❌ Docker error: {e.explanation}")
        return
    
if __name__ == '__main__':
    print(viewExistingContainers)
    
    inputUser = input("What will the username be for this container? : ")
    inputPassword = getpass("What will the password be for this container? : ")
    dbname = input("What will the name be for this container? : ")
    containerName = input("What do you want to name the container? : ")
    containerPort = input("What port will this run on? : ")
    
    createContainer(inputUser, inputPassword, dbname, containerName, containerPort, client)
