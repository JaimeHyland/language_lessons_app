import 'dart:convert';
import 'package:http/http.dart' as http;
import '../models/language.dart';
import '../models/level.dart';
import '../models/topic.dart';
import 'dart:io' show Platform;


class ApiService {
  static final String baseUrl = Platform.isAndroid
      ? 'http://10.0.2.2:8000'
      : 'http://127.0.0.1:8000';


  Future<List<Language>> fetchLanguages() async {
    final uri = Uri.parse('${ApiService.baseUrl}/api/languages/');
    final response = await http.get(uri);


    print('DEBUG: fetchLanguages: status=${response.statusCode}');
    print('DEBUG: fetchLanguages: body=${response.body}');

    if (response.statusCode == 200) {
      final List data = json.decode(response.body);
      return data.map((json) => Language.fromJson(json)).toList();
    } else {
      throw Exception('Failed to load languages');
    }
  }


  Future<List<Level>> fetchLevels() async {
    final uri = Uri.parse('${ApiService.baseUrl}/api/levels/');
    final response = await http.get(uri);

    if (response.statusCode == 200) {
      final List data = json.decode(response.body);
      return data.map((json) => Level.fromJson(json)).toList();
    } else {
      throw Exception('Failed to load levels');
    }
  }

  Future<List<Topic>> fetchTopics({
    required String languageIso,
    required int levelId,
  }) async {
    final uri = Uri.parse('${ApiService.baseUrl}/api/topics/').replace(
      queryParameters: {
        'language_iso': languageIso,
        'level_id': levelId.toString(),
      },
    );

    final response = await http.get(uri);

    if (response.statusCode == 200) {
      final List jsonList = json.decode(response.body);
      return jsonList.map((e) => Topic.fromJson(e)).toList();
    } else {
      throw Exception('Failed to load topics');
    }
  }
}

