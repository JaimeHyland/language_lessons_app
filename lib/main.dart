import 'package:flutter/material.dart';
import 'screens/welcome_screen.dart';
import 'screens/topics_page.dart';
import 'services/api_service.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    final apiService = ApiService();

    return MaterialApp(
      title: 'Language Lessons',
      theme: ThemeData(primarySwatch: Colors.blue),
      home: Builder(
        builder: (context) {
          WidgetsBinding.instance.addPostFrameCallback((_) {
            showDialog(
              context: context,
              barrierDismissible: false,
              builder: (_) => WelcomeScreen(
                apiService: apiService,
                onSubmit: (languageIso, levelId) {
                  Navigator.pushReplacement(
                    context,
                    MaterialPageRoute(
                      builder: (_) => TopicsPage(
                        languageIso: languageIso,
                        levelId: levelId,
                        apiService: apiService,
                      ),
                    ),
                  );
                },
              ),
            );
          });
          return const Scaffold(body: SizedBox());
        },
      ),
    );
  }
}
