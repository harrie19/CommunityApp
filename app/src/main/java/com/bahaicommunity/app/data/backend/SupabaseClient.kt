package com.bahaicommunity.app.data.backend

import io.github.jan_tennert.supabase.createSupabaseClient
import io.github.jan_tennert.supabase.gotrue.Auth
import io.github.jan_tennert.supabase.postgrest.Postgrest
import io.github.jan_tennert.supabase.realtime.Realtime

object SupabaseManager {

    // WICHTIG: Ersetzen Sie diese Platzhalter durch Ihre echten Supabase-Daten.
    // Sie finden diese in Ihrem Supabase-Projekt unter "Settings" -> "API".
    private const val SUPABASE_URL = "https://IHRE_PROJEKT_ID.supabase.co"
    private const val SUPABASE_ANON_KEY = "IHR_ANON_KEY"

    val client = createSupabaseClient(
        supabaseUrl = SUPABASE_URL,
        supabaseKey = SUPABASE_ANON_KEY
    ) {
        // Hier können Module installiert werden, die wir benötigen.
        install(Auth)
        install(Postgrest)
        install(Realtime)
    }
}
