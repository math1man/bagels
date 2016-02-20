package com.bagels.whatdo;

import com.google.api.server.spi.config.Api;
import com.google.api.server.spi.config.ApiMethod;
import com.google.api.server.spi.config.Nullable;

import javax.inject.Named;


/**
 * Add your first API methods in this class, or you may create another class. In that case, please
 * update your web.xml accordingly.
 **/
@SuppressWarnings("UnusedDeclaration")
@Api(name = "myApi",
        version = "v1",
        namespace = @ApiNamespace(ownerDomain = "helloworld.example.com",
                ownerName = "helloworld.example.com",
                packagePath=""))
public class EventApi {
}
