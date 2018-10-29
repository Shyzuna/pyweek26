# Operation MoonLight - Pyweek26
26th edition of the Pyweek GameJam.

Entry in PyWeek #26  <http://www.pyweek.org/26/>
Team: Operation MoonLight 
Members: Shyzuna PatatasFritas JambonBurst


DEPENDENCIES:

You might need to install some of these before running the game (without exe):

  Python:     3.6.7
  PyGame:     pip install pygame
  Numpy:      pip install numpy
  
  
BUILD WINDOWS EXECUTABLE:

  DEPENDENCIES:
   
    cx_Freeze: https://anthony-tuininga.github.io/cx_Freeze/
  
On Windows Move to the game directory and run:
  
  python setup.py build
  

RUNNING THE GAME:

On Windows, locate the "build\exe.win-amd64-3.6\main.exe" file and double-click it.

Otherwise open a terminal / console and "cd" to the game directory and run:

  python main.py


HOW TO PLAY THE GAME:

With mouse only.

    BUILD
	
You can build some buildings :
    * Gatherers: mine resources
	* Combiners: combine two resources into another one
	* Producers: produce ernergy
	* Capacitors: stock ernergy and resources
	* Connectors: connect buildings
	* Transmitter: sends energy to the earth (don't forget to connect it to the energy network)
	* Headquarter: you need to level up this building to unlock researches
	
Almost every building needs to be connected.
You can upgrade a building with the "Upgrade" button.

    RESEARCH

You can do some researches to improve you buildings or unlock new buildings.
New buildings give access to a new resource.
You have to upgrade the headquarter to access further levels.

	CONTRACT

You can earn credits by fulfiling contracts.
On the "Contracts" page, you can select a contract you want to accomplish.
You cannot change current contract unless you complete it.
To complete a contract, you need to send a certain amount or energy to the town specified in the contract (see "EARTH/SEND ENERGY" section)

    EARTH/SEND ERNERGY
	
The main goal of the game is to send energy to the earth.
Towns are connected only on certains hours. So if you want to send energy to a specific town, you have to wait the town to be accessible.
To send energy, you have to connect your transmitter to a working energy network.
Toggle the "Start sending/Stop sending" button to enable energy transfer. Don't forget to disable the transfer when you're done.
Energy is only send from batteries stock.


CREDITS :
  ARTS:
   * World Map (Pixel art) : http://pixelartmaker.com/art/d26e4686e0cce9c
  MUSIC:
   * Epic Blast Radius - Moon Lake : https://www.youtube.com/channel/UCOCJLwvBNwpNFJklCtaLqLg


LICENSE:

This game Operation Moonlight is placed in the Public Domain.

OVER JAM CHANGELOG :
* Fix on energy transmitter and battery causing crash in some situations.
* Fix overconsuming resources
* Adjust transmitter balance