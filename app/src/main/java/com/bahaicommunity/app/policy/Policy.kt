package com.bahaicommunity.app.policy

/**
 * Represents a single, verifiable policy rule.
 */
data class Policy(
    val id: String,
    val name: String,
    val description: String,
    val check: (request: PolicyRequest) -> PolicyResult
)

/**
 * Data class to hold the context of a request being evaluated.
 */
data class PolicyRequest(
    val intent: String,
    val generatedCode: String? = null
)

/**
 * Represents the outcome of a policy check.
 */
sealed class PolicyResult {
    object Allowed : PolicyResult()
    data class Denied(val reason: String) : PolicyResult()
}
