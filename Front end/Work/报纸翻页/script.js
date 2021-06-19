
// function flipToLeft(paper){
//     paper.css({'transform-origin': 'left center', 'animation': 'flip-to-left 2s ease-in-out forwards'});
//     paper.attr('data-left', '');
//     paper.removeAttr('data-right');
// }
// function flipToRight(paper){
//     paper.attr('data-right', '');
//     paper.removeAttr('data-left');
//     paper.css({'transform-origin': 'right center', 'animation': 'flip-to-right 2s ease-in-out forwards'});
// }

function dataRight(){
    let $rightPaper = $('.paper[data-right]');
    let $nextPaper = $rightPaper.next();
    if ($(".paper[data-left]").length){
        $rightPaper.attr('data-begin-animate', '');
        let $leftPaper = $('.paper[data-left]');
        $nextPaper.show();
        // flipToLeft($rightPaper);
        $leftPaper.hide();
    }
    else {
        $rightPaper.attr('data-begin-animate', '');
        $rightPaper.css('animation-fill-mode', 'forwards');
        $nextPaper.attr('data-right', '');
        $nextPaper.show();
        $rightPaper.attr('data-left', '');
        $rightPaper.removeAttr('data-right');
    }
}



