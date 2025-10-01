// ignore: unused_import
import 'package:intl/intl.dart' as intl;
import 'app_localizations.dart';

// ignore_for_file: type=lint

/// The translations for English (`en`).
class AppLocalizationsEn extends AppLocalizations {
  AppLocalizationsEn([String locale = 'en']) : super(locale);

  @override
  String get text_welcome => 'Welcome!';

  @override
  String get dropdown_select_language => 'Select language';

  @override
  String get dropdown_select_level => 'Select level';

  @override
  String get button_continue => 'Continue';
}
