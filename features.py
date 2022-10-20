"""
Program to displays various pictures from NASA.
 -  Astronomy Picture of the Day
"""
import sys
import requests
import webbrowser
import os

class AstronomyPy:
    def __init__(self):
        self.get_api()
        self.URL = "https://api.nasa.gov/planetary/apod?api_key="
        self.consent()
    
    def get_api(self):
        with open("./my_api.txt", "r") as f:
            __myapi__=f.read()
        if __myapi__ == "":
            self.__myapi__=input("API: ")
            with open("./my_api.txt", "w") as f:
                f.write(self.__myapi__)
        else:
            self.__myapi__=__myapi__

    def consent(self):
        self.op = str(input("Continue? ")).lower().strip()
        if self.op == "yes":
            self.makeRequest()
        else:
            sys.exit("Exiting...")

    def makeRequest(self):
        self.req = requests.get("https://api.nasa.gov/planetary/apod?api_key="+self.__myapi__)
        self.req = self.req.json()
        self.description = self.req["explanation"]
        self.imgUrl = self.req["hdurl"]
        self.title = self.req["title"]
        self.date = self.req["date"]
        self.editPage()
    
    def editPage(self):
        html_page =f"""
        <html>
            <title>{self.title}</title>
        <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=100.0">
        <script src="https://cdn.tailwindcss.com"></script>
        <br><br>
        <center><h1 class="text-2xl"><b>Astronomy Picture of the Day</b></h1></center>
        </head>
        <body>
        <section class="text-gray-600 body-font">
            <div class="container mx-auto flex px-5 py-24 items-center justify-center flex-col">
                <img class="lg:w-2/6 md:w-3/6 w-5/6 mb-10 object-cover object-center rounded" src={self.imgUrl} alt="pic">
                <div class="text-center lg:w-2/3 w-full">
                    <h1 class="title-font sm:text-4xl text-3xl mb-4 font-medium text-gray-900">{self.title}</h1>
                    <p class="mb-8 leading-relaxed">{self.description}<h3><b>Date: {self.date}</b></h3></p>
                    <br><br>
                    <div class="flex justify-center">
                        <a href="{self.imgUrl}" download="pic">
                    <button class="inline-flex text-white bg-indigo-500 border-0 py-2 px-6 focus:outline-none hover:bg-indigo-600 rounded text-lg">Download</button>
                    </a>
                    </div>
                </div>
            </div>
        </section>

        <footer class="text-gray-600 body-font">
            <div class="container px-5 py-8 mx-auto flex items-center sm:flex-row flex-col">
                <p class="text-sm text-gray-500 sm:ml-4 sm:pl-4 sm:border-l-2 sm:border-gray-200 sm:py-2 sm:mt-0 mt-4">Project IMAPI  -
                <a href="https://github.com/Mayuresh-22" class="text-gray-600 ml-1" rel="noopener noreferrer" target="_blank">Mayuresh-22</a>
                </p>
            </div>
        </footer>
        </body>
        </html>
        """
        with open("index.html", "w") as f:
            f.write(html_page)
        print("Updated...")
        webbrowser.open('file://'+os.path.realpath("index.html"))

class MarsRoverPic:
    pass

# obj = AstronomyPy()
