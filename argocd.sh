argocd app create us-mlpredictor \
	--repo https://github.com/kurisujhin/CS401-Proj2 \
	--path . \
	--project tz88-project \
	--dest-namespace tz88 \
	--dest-server https://kubernetes.default.svc \
	--sync-policy auto