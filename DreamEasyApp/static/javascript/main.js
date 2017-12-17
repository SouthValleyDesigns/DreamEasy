var options = {
	classname: 'my-class',
  id: 'my-id',
	target: document.getElementById('myDivId')
};

var nanobar = new Nanobar( options );

//move bar
nanobar.go( 30 ); // size bar 30%
nanobar.go( 76 ); // size bar 76%

// size bar 100% and and finish
nanobar.go(100);
