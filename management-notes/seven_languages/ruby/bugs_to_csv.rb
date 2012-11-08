require "open-uri" 
#require "uri"
require "./csv_to_tasks"

COMMA_URL_ENCODED = '%2C'
VALID_COLUMNS = ['changeddate', 'bug_severity','priority','actual_time','assigned_to','assigned_to_realname','bug_status','estimated_time','resolution','component','remaining_time','short_desc','cf_time_category','target_milestone','cf_release_notes','cf_customer']


def bugzilla_query_string(query={},
                          columns=[],
                          output_format="csv",
                          base_url="http://bugzilla/bugzilla/buglist.cgi")


    query_defaults = {:product => "",
                      :target_milestone => "",
                      :priority => "P1",
                      :bug_status => ["UNCONFIRMED", "CONFIRMED"]}
    query = query_defaults.merge(query)

    column_defaults = ["remaining_time", "short_desc"]
    columns = column_defaults | columns

    columns.each do |column|
        unless VALID_COLUMNS.member? column
            raise ArgumentError, "Column '#{column}' must be one of '#{VALID_COLUMNS.join(", ")}'"
        end
    end

    # Add the column required as a comma separated values
    query[:columnlist] = columns.join(',')

    # Add the output format
    query[:ctype] = output_format

    # Turn the array into a URL with query params that Bugzilla will accept
    base_url + '?' + URI.encode_www_form(query)

end


def bugs_to_csv(output="bugs.csv")

    # Test invalid columns
    #query_string = bugzilla_query_string(123, ['bob','phil'])
    # Test invalid number
    #query_string = bugzilla_query_string(0, ['bob','phil'])

    query_string = bugzilla_query_string({:product => "Development",
                                         :target_milestone => "v6.1.0",
                                         :priority => "MUST",
                                         :bug_status => ["UNCONFIRMED",
                                                         "CONFIRMED",
                                                         "WAITING_ON_CUSTOMER",
                                                         "WAITING_ON_DEV",
                                                         "WAITING_ON_EA",
                                                         "WAITING_ON_TS",
                                                         "REOPENED"]},
                                         ["remaining_time",
                                          "short_desc",
                                          "assigned_to",
                                          "cf_time_category",
                                          "target_milestone",
                                          "estimated_time",
                                          "actual_time",
                                          "cf_release_notes",
                                          "cf_customer"]
                                        )
    puts "# " + query_string

    uri = URI.parse(query_string)


    converter = CsvTaskConverter.new(:csv_column_mapping => {
                                         :id => "bug_id",
                                         :name => "short_desc",
                                         :effort => "remaining" })

    # read it as a string
    bug_list = uri.read
    #puts bug_list

    converter.csv_string_to_tasks(bug_list)
    #converter.csv_file_to_tasks(uri.open)

end

bugs_to_csv
