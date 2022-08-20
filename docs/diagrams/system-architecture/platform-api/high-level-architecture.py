from diagrams import Cluster, Diagram, Edge
from diagrams.aws.compute import Lambda
from diagrams.aws.database import DynamodbTable
from diagrams.aws.general import SDK
from diagrams.aws.network import APIGateway
from diagrams.aws.security import Cognito

with Diagram("High-level-architecture", show=False):
    sdk = SDK("SDK")

    with Cluster("Platform API"):
        with Cluster("FrontEnd"):
            auth = Cognito("Auth")
            reverse_proxy = APIGateway("ReverseProxy")

        with Cluster("BackEnd"):
            request_handler = Lambda("RequestHandler")

            with Cluster("Database"):
                database = [
                    DynamodbTable("User"),
                    DynamodbTable("Skills"),
                ]

        sdk >> Edge(label="(1) authenticate") >> auth
        sdk >> Edge(label="(2) send request") >> reverse_proxy
        auth << Edge(label="(3) authorize") << reverse_proxy
        reverse_proxy >> Edge(label="(4) proxy request") >> request_handler
        request_handler >> Edge(label="(5) read/write data") >> database
