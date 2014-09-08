// Loads Facebook SDK for Javacript
$(document).ready(function() {
    $.ajaxSetup({ cache: true });

    $.getScript('//connect.facebook.net/en_US/all.js', function() {
        FB.init({
            appId: '1457668654508174',
            status: true,
            cookie: true,
            xfml: true,
            channelUrl: '//localhost:8000/channel.html',
            version: 'v2.1'
        });
        FB.getLoginStatus(function(response) {
            statusChangeCallback(response);
        });
    });

    $('button.facebook').click(function(e) {
        FB.login(function(response) {
        }, {scope: 'public_profile,email'});
        e.preventDefault();
        e.stopPropagation();
    });
});
