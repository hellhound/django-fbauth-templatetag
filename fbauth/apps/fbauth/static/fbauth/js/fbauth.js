var fbFacade = {
    isConnected: function(response) {
        return response.status == 'connected';
    },
    onLogin: function(response) {
        var self = this;

        if (self.isConnected(response)) {
            window.location.href = '/facebook/login/success?access_token='
                + response.authResponse.accessToken;
        }
    },
    getLoginStatus: function() {
        var self = this;

        FB.getLoginStatus(function(response) {
            if (self.isConnected(response)) {
                self.onLogin(response);
            }
            else {
                FB.login(
                    self.onLogin,
                    {scope: 'public_profile,email'}
                );
            }
        });
    },
    init: function() {
        // Loads Facebook SDK for Javacript
        $.ajaxSetup({ cache: true });

        $.getScript('//connect.facebook.net/en_US/all.js', function() {
            FB.init({
                appId: '1457668654508174',
                status: true,
                cookie: true,
                xfml: true,
                channelUrl: '//localhost:8000/static/fbauth/html/channel.html',
                version: 'v2.1'
            });
            FB.getLoginStatus(function(response) {
                statusChangeCallback(response);
            });
        });
    }
};

$(document).ready(function() {
    fbFacade.init();

    $('button.facebook').click(function(e) {
        fbFacade.getLoginStatus();
        e.preventDefault();
        e.stopPropagation();
    });
});
