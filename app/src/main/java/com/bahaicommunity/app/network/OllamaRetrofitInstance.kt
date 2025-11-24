package com.bahaicommunity.app.network

import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory

/**
 * A separate Retrofit instance specifically for connecting to the Ollama server.
 */
object OllamaRetrofitInstance {

    // This will be confirmed by the user later. For now, we use the default.
    private const val BASE_URL = "http://localhost:11434/"

    val api: OllamaApiService by lazy {
        Retrofit.Builder()
            .baseUrl(BASE_URL)
            .addConverterFactory(GsonConverterFactory.create())
            .build()
            .create(OllamaApiService::class.java)
    }
}
