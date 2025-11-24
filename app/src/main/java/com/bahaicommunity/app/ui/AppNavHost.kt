package com.bahaicommunity.app.ui

import androidx.compose.runtime.Composable
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController

@Composable
fun AppNavHost(viewModel: AppBuilderViewModel) {
    val navController = rememberNavController()

    NavHost(navController = navController, startDestination = "builder") {
        composable("builder") {
            AppBuilderScreen(
                viewModel = viewModel,
                onShowLogsClicked = { navController.navigate("logs") }
            )
        }
        composable("logs") {
            val records by viewModel.auditLogState.collectAsState()
            AuditLogScreen(records = records)
        }
    }
}
