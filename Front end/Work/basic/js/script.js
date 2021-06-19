
let minScale = 1, interval = 0.1;
let width, height, maxScale;
let img, w, h;
let scale = 1;

function flipbookClick(){
    if($('.page-wrapper:visible').length === 2)
        flipbook.css('transform', 'translateX('+(-(width/2*scale))+'px) scale('+ scale +')');
    else
        flipbook.css('transform', 'scale('+ scale +')');
}

function flipbookdblclick(e){
    let X = e.pageX;
    let Y = e.pageY;

    // if (scale === 1) {
    //     scale = maxScale;
    //     if($('.page-wrapper:visible').length === 2)
    //         flipbook.css('transform', 'translate('+X+'px, '+Y+'px) scale('+ scale +')');
    //     else
    //         flipbook.css('transform', 'scale('+ scale +')');
    // } else {
    //     scale = 1;
    // }
    // console.log(X);
    // flipbookClick();
}

function loadApp() {

    img = flipbook.find('img').get(0);
    w = window.innerWidth * 0.9 / img.width / 2;
    h = window.innerHeight * 0.9 / img.height;
    if (w > h){
        width = img.width * h;
        height = img.height * h;
        maxScale = 1 / h;
    }else {
        height = img.height * w;
        width = img.width * w;
        maxScale = 1 / w;
    }
    flipbook.turn({
        width:width * 2,
        height:height,
        elevation: 50,
        gradients: true,
        autoCenter: false
    });

    // let css = flipbook.css('transform') + 'translateX('+(-(width/2*scale))+'px)';
    // flipbook.css('transform', css);
    $('body').css({'width':window.innerWidth+'px', 'height':window.innerHeight+'px'});
    $('.flipbook-viewport .container').css({'width':window.innerWidth+'px', 'height':window.innerHeight+'px'});
    flipbook.find('img').show();

    // flipbook.bind('click', flipbookClick);
    // flipbook.bind('dblclick', flipbookdblclick);

}

yepnope({
    test : Modernizr.csstransforms,
    yep: ['js/turn.min.js'],
    both: ['css/basic.css'],
    complete: loadApp
});

