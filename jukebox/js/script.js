$(function() {

    initializeClicks();



});


function initializeClicks() {

    $('.playButton').click(function() {
        var fileName = $(this).closest("tr").find(".fileName").text();
        alert(fileName);
        if ($(this).closest("tr").hasClass("folder")) {
            var folderId = $(this).closest("tr").attr("id");
            $("." + folderId).hide();
        }
    });

    initFolderClick();
}

function initFolderClick() {
    $('.fileName').click(function() {
        if ($(this).closest("tr").hasClass("folder") && $(this).closest("tr").hasClass("closed")) {
            var folderId = $(this).closest("tr").attr("id");
            $("." + folderId).show();
            $(this).closest("tr").removeClass("closed");
            $(this).closest("tr").addClass("open");
        } else if ($(this).closest("tr").hasClass("folder") && $(this).closest("tr").hasClass("open")) {
            var folderId = $(this).closest("tr").attr("id");
            $("." + folderId).hide();
            $(this).closest("tr").removeClass("open");
            $(this).closest("tr").addClass("closed");
        }
    })
}