package com.bahaicommunity.app.policy

/**
 * The core Policy Engine. It evaluates a request against a set of policies.
 */
class PolicyEngine(private val policies: List<Policy>) {

    /**
     * Evaluates the given request against all loaded policies.
     *
     * @return The first `Denied` result found, or `Allowed` if all policies pass.
     */
    fun evaluate(request: PolicyRequest): PolicyResult {
        for (policy in policies) {
            when (val result = policy.check(request)) {
                is PolicyResult.Denied -> {
                    // If any policy denies the request, return immediately.
                    return result
                }
                is PolicyResult.Allowed -> {
                    // Continue to the next policy.
                }
            }
        }
        // If all policies passed, the request is allowed.
        return PolicyResult.Allowed
    }
}
