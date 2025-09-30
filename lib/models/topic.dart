class Topic {
  final int id;
  final String key;
  final String nativeName;
  final Map<String, dynamic> foreignNames;
  final int order;
  final String themeName;
  final String languageIso;
  final int levelId;

  Topic({
    required this.id,
    required this.key,
    required this.nativeName,
    required this.foreignNames,
    required this.order,
    required this.themeName,
    required this.languageIso,
    required this.levelId,
  });

  factory Topic.fromJson(Map<String, dynamic> json) {
    return Topic(
      id: json['id'],
      key: json['key'],
      nativeName: json['native_name'],
      foreignNames: Map<String, dynamic>.from(json['foreign_names']),
      order: json['order'],
      themeName: json['theme_name'],
      languageIso: json['language_iso'],
      levelId: json['level'],
    );
  }
}
