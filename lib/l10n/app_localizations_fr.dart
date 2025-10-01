// ignore: unused_import
import 'package:intl/intl.dart' as intl;
import 'app_localizations.dart';

// ignore_for_file: type=lint

/// The translations for French (`fr`).
class AppLocalizationsFr extends AppLocalizations {
  AppLocalizationsFr([String locale = 'fr']) : super(locale);

  @override
  String get text_welcome => 'Bienvenue!';

  @override
  String get dropdown_select_language => 'Sélectionnez la langue';

  @override
  String get dropdown_select_level => 'Sélectionnez le niveau';

  @override
  String get button_continue => 'Continuer';
}
