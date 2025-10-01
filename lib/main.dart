import 'package:flutter/material.dart';
import 'screens/welcome_screen.dart';
import 'screens/topics_page.dart';
import 'services/api_service.dart';
import 'package:flutter_localizations/flutter_localizations.dart';
import 'package:language_lessons_app/l10n/app_localizations.dart';


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
      localizationsDelegates: const [
        GlobalMaterialLocalizations.delegate,
        GlobalWidgetsLocalizations.delegate,
        GlobalCupertinoLocalizations.delegate,
      ],
      supportedLocales: const [
        Locale('en'),
        Locale('de'),
        Locale('es'),
        Locale('fr'),
        Locale('ga'),
        Locale('eu'),
      ],
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
