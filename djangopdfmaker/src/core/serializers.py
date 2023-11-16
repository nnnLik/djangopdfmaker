from rest_framework import serializers


class GeneratePdfFromSourceSerializer(serializers.Serializer):
    url = serializers.URLField(required=False)
    file = serializers.FileField(required=False)

    def validate(self, data):
        url = data.get("url")
        file = data.get("file")

        if not url and not file:
            raise serializers.ValidationError("Provide either URL or HTML file.")

        if url and file:
            raise serializers.ValidationError(
                "Provide either URL or HTML file, not both."
            )

        return self.validate_and_prepare_data(url, file)

    def validate_and_prepare_data(self, url, file):
        if url:
            return {"to_pdf": url, "type": "url"}

        if not file.name.endswith(".html"):
            raise serializers.ValidationError(
                "Invalid file format. Please provide an HTML file."
            )

        return {"to_pdf": file, "type": "file"}
