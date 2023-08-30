
all: next-training.csv next-activity.csv

require_scouts_password:
ifndef SCOUTS_USERNAME
	$(error SCOUTS_USERNAME is not defined)
endif
ifndef SCOUTS_PASSWORD
	$(error SCOUTS_PASSWORD is not defined)
endif
ifndef SCOUTS_PROFILE_ID
	$(error SCOUTS_PROFILE_ID is not defined)
endif

next-training.json: require_scouts_password
	python get-next-training.py > next-training.json

next-training.csv: next-training.json
	echo "StartDate,CanBook,Location,Title" > next-training.csv
	cat next-training.json | jq -r '.[] | [.StartDate,.CanBook,.LocationTitle,.Title] | @csv' | tac >> next-training.csv

next-activity.json: require_scouts_password
	python get-next-training.py --activity > next-activity.json

next-activity.csv: next-activity.json
	echo "StartDate,CanBook,Location,Title" > next-activity.csv
	cat next-activity.json | jq -r '.[] | [.StartDate,.CanBook,.LocationTitle,.Title] | @csv' | tac >> next-activity.csv

clean:
	rm -f next-training.json next-training.csv next-activity.json next-activity.csv
