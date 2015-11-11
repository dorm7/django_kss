(function(global){
    'use strict';

    var $ = global.$;

    var replaceIframe = global.replaceIframe = function(config){

        console.log(config.target);
        console.log(config.source);

        var source = $(config.source).text();
        console.log(source)

        $(config.target)
            .contents()
            .find('body')
            .html(
                source
            );
    };

})(window);
