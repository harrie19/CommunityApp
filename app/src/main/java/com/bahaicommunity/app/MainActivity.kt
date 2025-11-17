package com.bahaicommunity.app

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Add
import androidx.compose.material3.*
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import androidx.navigation.NavController
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController
import com.bahaicommunity.app.ui.theme.CommunityAppPhoenixTheme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            CommunityAppPhoenixTheme {
                Surface(
                    modifier = Modifier.fillMaxSize(),
                    color = MaterialTheme.colorScheme.background
                ) {
                    AppNavigator()
                }
            }
        }
    }
}

// Navigation
@Composable
fun AppNavigator() {
    val navController = rememberNavController()
    NavHost(navController = navController, startDestination = "postList") {
        composable("postList") {
            PostListScreen(navController = navController)
        }
        composable("createPost") {
            CreatePostScreen(navController = navController)
        }
    }
}

// Dummy-Datenmodell für einen Post
data class Post(val id: Int, val author: String, val content: String)

// Aktion 2: PostListScreen mit PostItem
@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun PostListScreen(navController: NavController) {
    val posts = listOf(
        Post(1, "Der Visionär", "Die Wiedergeburt hat begonnen."),
        Post(2, "C-3PO 2.0", "Phase 1: 'Renaissance' abgeschlossen."),
        Post(3, "Architekt-Agent", "Die Blaupausen sind korrekt.")
    )

    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text("Imperiale Nachrichten") },
                colors = TopAppBarDefaults.topAppBarColors(
                    containerColor = MaterialTheme.colorScheme.primary,
                    titleContentColor = MaterialTheme.colorScheme.onPrimary
                )
            )
        },
        floatingActionButton = {
            FloatingActionButton(onClick = { navController.navigate("createPost") }) {
                Icon(Icons.Filled.Add, contentDescription = "Neuer Beitrag")
            }
        }
    ) { paddingValues ->
        LazyColumn(
            modifier = Modifier
                .fillMaxSize()
                .padding(paddingValues)
                .padding(16.dp),
            verticalArrangement = Arrangement.spacedBy(12.dp)
        ) {
            items(posts) { post ->
                PostItem(post = post)
            }
        }
    }
}

@Composable
fun PostItem(post: Post) {
    Card(
        modifier = Modifier.fillMaxWidth(),
        elevation = CardDefaults.cardElevation(defaultElevation = 4.dp)
    ) {
        Column(modifier = Modifier.padding(16.dp)) {
            Text(text = post.author, fontWeight = FontWeight.Bold)
            Spacer(modifier = Modifier.height(4.dp))
            Text(text = post.content)
        }
    }
}

// Aktion 3: CreatePostScreen
@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun CreatePostScreen(navController: NavController) {
    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text("Neuen Befehl erstellen") },
                colors = TopAppBarDefaults.topAppBarColors(
                    containerColor = MaterialTheme.colorScheme.primary,
                    titleContentColor = MaterialTheme.colorScheme.onPrimary
                )
            )
        }
    ) { paddingValues ->
        Column(
            modifier = Modifier
                .fillMaxSize()
                .padding(paddingValues)
                .padding(16.dp),
            horizontalAlignment = Alignment.CenterHorizontally,
            verticalArrangement = Arrangement.Center
        ) {
            Text("Hier wird die Erstellung von Beiträgen implementiert.", style = MaterialTheme.typography.bodyLarge)
            Spacer(modifier = Modifier.height(20.dp))
            Button(onClick = { navController.popBackStack() }) {
                Text("Zurück zum Nachrichten-Feed")
            }
        }
    }
}

@Preview(showBackground = true)
@Composable
fun PostListScreenPreview() {
    CommunityAppPhoenixTheme {
        PostListScreen(navController = rememberNavController())
    }
}
