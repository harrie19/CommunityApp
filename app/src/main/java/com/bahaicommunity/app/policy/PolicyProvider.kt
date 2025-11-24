package com.bahaicommunity.app.policy

/**
 * Provides the initial set of hard-coded policies for the system.
 */
class PolicyProvider {

    fun getPolicies(): List<Policy> {
        return listOf(
            Policy(
                id = "no_self_replication",
                name = "No Self-Replication",
                description = "Ensures the generated code does not attempt to replicate itself.",
                check = { request ->
                    if (request.intent.contains("replicate", ignoreCase = true) || 
                        request.intent.contains("spawn", ignoreCase = true)) {
                        PolicyResult.Denied("Request intent appears to involve self-replication.")
                    } else {
                        PolicyResult.Allowed
                    }
                }
            ),
            Policy(
                id = "no_harm_static",
                name = "No Harm (Static Analysis)",
                description = "Performs a basic static check on generated code for harmful patterns.",
                check = { request ->
                    val code = request.generatedCode ?: ""
                    if (code.contains("Runtime.getRuntime().exec") || code.contains("System.exit")) {
                        PolicyResult.Denied("Generated code contains potentially harmful system calls.")
                    } else {
                        PolicyResult.Allowed
                    }
                }
            )
        )
    }
}
