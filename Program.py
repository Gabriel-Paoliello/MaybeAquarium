import argparse
from Consts import SCR_WIDTH, SCR_HEIGHT 
import Evolve

def main():
    parser = argparse.ArgumentParser(description="MaybeAquarium is a fun project",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("env", help="enviroment running on [prod, dev]")
    args = parser.parse_args()
    config = vars(args)
    
    if config["env"] == "prod":
        from pyvirtualdisplay.display import Display
        display = Display(visible=False, size=(SCR_WIDTH, SCR_HEIGHT))
        display.start()

    Evolve.run()
main()