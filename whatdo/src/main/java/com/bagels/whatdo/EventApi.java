package com.bagels.whatdo;

import com.bagels.whatdo.model.Event;
import com.google.api.server.spi.ServiceException;
import com.google.api.server.spi.config.Api;
import com.google.api.server.spi.config.ApiMethod;
import com.google.api.server.spi.config.ApiNamespace;


/**
 * Add your first API methods in this class, or you may create another class. In that case, please
 * update your web.xml accordingly.
 **/
@SuppressWarnings("UnusedDeclaration")
@Api(name = "whatdo",
        version = "v1",
        namespace = @ApiNamespace(ownerDomain = "whatdo.bagels.com",
                ownerName = "whatdo.bagels.com",
                packagePath=""))
public class EventApi {

    @ApiMethod(name = "whatdoApi.getUser",
            path = "event/random",
            httpMethod = ApiMethod.HttpMethod.GET)
    public Event getRandomEvent() throws ServiceException {
        return new Event("Walker Art Center", "http://www.walkerart.org/",
                "$9-14 per person", "Varies", "Any", "8 miles",
                "The Walker Art Center is a multidisciplinary contemporary art center. " +
                "The Walker is considered one of America\'s premier museums for modern art."
        );
    }

}
