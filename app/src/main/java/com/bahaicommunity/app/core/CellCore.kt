package com.bahaicommunity.app.core

import com.bahaicommunity.app.network.OllamaApiService
import com.bahaicommunity.app.network.OllamaRequest

/**
 * The Cell Core is responsible for the main logic, including code generation.
 */
class CellCore(private val ollamaApi: OllamaApiService) {

    /**
     * Generates code by sending a formatted prompt to the Ollama LLM.
     */
    suspend fun generateCode(description: String): String {
        return try {
            // Format a specific prompt for the code generation task
            val prompt = """
                You are an expert Android developer. 
                Generate a single, complete, and syntactically correct Kotlin file for a simple Android app 
                based on the following description. Do not add any explanations, just the code.

                Description: "$description"
            """".trimIndent()

            val request = OllamaRequest(
                model = "codegemma", // A sensible default model
                prompt = prompt
            )

            val response = ollamaApi.generate(request)
            response.response
        } catch (e: Exception) {
            // In case of network errors, return a descriptive error message.
            "Error generating code: ${e.message}"
        }
    }
}
