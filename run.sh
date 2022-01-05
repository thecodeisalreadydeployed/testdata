cd $(dirname $0)

gh repo clone thecodeisalreadydeployed/testdata workspace
cd workspace

git switch testdata
# echo "// $(date --iso-8601=seconds)\n\n$(cat nx/apps/nest-a/src/main.ts)" > nx/apps/nest-a/src/main.ts
sed -i "1s/.*/\/\/ $(date --iso-8601=seconds)/" ./nx/apps/nest-a/src/main.ts

git add nx/apps/nest-a/src/main.ts
git commit -m "$(date --iso-8601=seconds)"
git push

cd ../
rm -rf ./workspace
