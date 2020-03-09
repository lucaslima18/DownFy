import argparse

parser = argparse.ArgumentParser(description="")
parser.add_argument("--link", required=False,default="", type=str)
parser.add_argument("--service", required=True, type=str)
arguments = parser.parse_args()

SERVICE = arguments.service
LINK = arguments.link

if (
    arguments.service == "playlist"
    or arguments.service == "albun"
    or arguments.service == "music"
):
    SERVICE_TYPE = arguments.service

else:
    #deixar textos mais completos aqui
    print("\nThis option is not avaliable, please reload and try one of this options:\n")
    print("playlist\nalbun\nmusic\n")
    exit()