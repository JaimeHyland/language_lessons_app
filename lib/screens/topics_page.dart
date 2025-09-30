import 'package:flutter/material.dart';
import '../models/topic.dart';
import '../services/api_service.dart';

class TopicsPage extends StatefulWidget {
  final String languageIso;
  final int levelId;
  final ApiService apiService;

  const TopicsPage({
    required this.languageIso,
    required this.levelId,
    required this.apiService,
    super.key,
  });

  @override
  State<TopicsPage> createState() => _TopicsPageState();
}

class _TopicsPageState extends State<TopicsPage> {
  late Future<List<Topic>> topicsFuture;

  @override
  void initState() {
    super.initState();
    topicsFuture = widget.apiService.fetchTopics(
        languageIso: widget.languageIso,
        levelId: widget.levelId);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Topics')),
      body: FutureBuilder<List<Topic>>(
        future: topicsFuture,
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            return const Center(child: CircularProgressIndicator());
          } else if (snapshot.hasError) {
            return Center(child: Text('Error: ${snapshot.error}'));
          } else {
            final topics = snapshot.data!;
            if (topics.isEmpty) {
              return const Center(child: Text('No topics found.'));
            }
            return ListView.builder(
              itemCount: topics.length,
              itemBuilder: (context, index) {
                final topic = topics[index];
                return ListTile(
                  title: Text(topic.nativeName),
                  subtitle: Text('${topic.themeName} (${topic.languageIso})'),
                );
              },
            );
          }
        },
      ),
    );
  }
}
