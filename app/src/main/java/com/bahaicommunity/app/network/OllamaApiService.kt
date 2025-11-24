package com.bahaicommunity.app.network

import retrofit2.http.Body
import retrofit2.http.POST

/**
 * Retrofit API service interface for communicating with the Ollama server.
 */
interface OllamaApiService {

    @POST("api/generate")
    suspend fun generate(@Body request: OllamaRequest): OllamaResponse

}
