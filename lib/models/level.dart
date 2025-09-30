class Level {
  final int id;
  final String code;
  final int order;

  Level({required this.id, required this.code, required this.order});

  factory Level.fromJson(Map<String, dynamic> json) {
    return Level(
      id: json['id'],
      code: json['code'],
      order: json['order'],
    );
  }
}
