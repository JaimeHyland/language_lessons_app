class Language {
  final int id;
  final String displayName;
  final String isoCode;

  Language({required this.id, required this.displayName, required this.isoCode});

  factory Language.fromJson(Map<String, dynamic> json) {
    return Language(
      id: json['id'],
      isoCode: json['iso_code'],
      displayName: json['display_name'], // matches Django backend field
    );
  }
}
