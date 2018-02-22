$(document).ready(function() {
    var options = {
    	classname: 'paper',
    };

    var nanobar = new Nanobar( options );

    //move bar
    nanobar.go( 30 ); // size bar 30%
    nanobar.go( 76 ); // size bar 76%

    // size bar 100% and and finish
    nanobar.go(100);

    $('#pagination-demo').twbsPagination({
    totalPages: 35,
    visiblePages: 7,
    onPageClick: function (event, page) {
        $('#page-content').text('Page ' + page);
    }
    });
});
