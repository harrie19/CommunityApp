package com.bahaicommunity.app.network

import com.google.gson.annotations.SerializedName

/**
 * Data class for sending a request to the Ollama API.
 */
data class OllamaRequest(
    val model: String,
    val prompt: String,
    val stream: Boolean = false
)

/**
 * Data class for receiving a response from the Ollama API.
 */
data class OllamaResponse(
    val model: String,
    val response: String,
    @SerializedName("done")
    val isDone: Boolean
)
