{{/*
Generate a full name with the release name included to avoid name conflicts
*/}}
{{- define "restapi-app.fullname" -}}
{{- printf "%s-%s" .Release.Name .Chart.Name | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/*
Generate a name for the application
*/}}
{{- define "restapi-app.name" -}}
{{- .Chart.Name -}}
{{- end -}}