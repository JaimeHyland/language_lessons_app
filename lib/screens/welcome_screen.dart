import 'package:flutter/material.dart';
import '../models/language.dart';
import '../models/level.dart';
import '../services/api_service.dart';

class WelcomeScreen extends StatefulWidget {
  final ApiService apiService;
  final Function(String languageIso, int levelId) onSubmit;

  const WelcomeScreen({
    required this.apiService,
    required this.onSubmit,
    super.key
  });

  @override
  State<WelcomeScreen> createState() => _WelcomeScreenState();
}

class _WelcomeScreenState extends State<WelcomeScreen> {
  List<Language> languages = [];
  List<Level> levels = [];
  Language? selectedLanguage;
  Level? selectedLevel;

  @override
  void initState() {
    super.initState();
    _loadData();
  }

  Future<void> _loadData() async {
    print('DEBUG: Running _loadData');
    final availableLanguages = await widget.apiService.fetchLanguages();
    final availableLevels = await widget.apiService.fetchLevels();

    print('DEBUG: Languages: $availableLanguages');
    print('DEBUG: Levels: $availableLevels');

    setState(() {
      languages = availableLanguages;
      levels = availableLevels;
    });
  }

  @override
  Widget build(BuildContext context) {
    return AlertDialog(
      title: const Text('Welcome!'),
      content: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          DropdownButton<Language>(
            hint: Text('Select language'),
            value: selectedLanguage,
            onChanged: (languageOption) =>
                setState(() => selectedLanguage = languageOption),
            items: languages
                .map((languageOption) => DropdownMenuItem(
                    value: languageOption,
                    child: Text(languageOption.isoCode),
                  ))
                .toList(),

          ),
          DropdownButton<Level>(
            hint: Text('Select level'),
            value: selectedLevel,
            onChanged: (levelOption) =>
                setState(() => selectedLevel = levelOption),
            items: levels
                  .map((levelOption) => DropdownMenuItem(
                    value: levelOption,
                    child: Text(levelOption.code),
            ))
                .toList(),
          ),
        ],
      ),
      actions: [
        TextButton(
          onPressed: (selectedLanguage != null && selectedLevel != null)
              ? () {
            widget.onSubmit(
                selectedLanguage!.isoCode,
                selectedLevel!.id
            );
            Navigator.of(context).pop();
          }
              : null,
          child: const Text('Continue'),
        ),
      ],
    );
  }
}
