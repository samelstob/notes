
require "csv"

class CsvTaskConverter
    # Mapping of CSV columns to TJ task attributes
    DEFAULT_OPTIONS = {
        :csv_column_mapping => { :id => "bug_id",
                                 :name => "short_desc",
                                 :effort => "remaining" },

        :task_defaults => { :effort => "4d # default effort" }
    }


    def initialize(options = {})
        options = DEFAULT_OPTIONS.merge(options) 

        @csv_column_mapping = options[:csv_column_mapping]
        @task_defaults = options[:task_defaults]
    end

    def task_to_s(task={})
        # check that task_id is a valid identifier

        # Merge needs to merge nil values in an intelligent way
        # Sometimes we want Nil, sometimes we want NVL(csv, default)
        task.delete_if { |k, v| v.nil? }

        task = @task_defaults.merge(task)

        # Replace illegal characters in task attributes
        task.each do |k, v|
            task[k] = v.tr('"', "'")
        end

        return "task #{task[:id]} \"#{task[:name]}\" {
                  effort #{task[:effort]}
              }
        "
    end


    def handle_csv_row(row)
        task = { :id => "bug#{row[@csv_column_mapping[:id]]}",
                 :name => row[@csv_column_mapping[:name]],
                 :effort => row[@csv_column_mapping[:effort]] }
        puts task_to_s(task)
    end

    def csv_file_to_tasks(file)

        # Might be nice to validate that the columns exist in the CSV

        # Read file and parse as CSV
        CSV.foreach(file, :headers => true) do |row|
            handle_csv_row(row)
        end
    end

    def csv_string_to_tasks(csv_string="")
        # Might be nice to validate that the columns exist in the CSV

        # Read file and parse as CSV
        CSV.parse(csv_string, :headers => true) do |row|
            handle_csv_row(row)
        end
    end

end

#converter = CsvTaskConvertor.new()
#converter.csv_file_to_tasks("tasks.csv")

