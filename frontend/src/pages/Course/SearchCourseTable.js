
import React, { useEffect, useState } from 'react'
import { filterGreaterThan, NumberRangeColumnFilter, SliderColumnFilter, Styles, SelectColumnFilter} from './Filters'
import { get } from 'utils/sdk'
import {Table} from "./Table";
import {Button} from "react-bootstrap";
import {useNavigate} from "react-router-dom";
// Our table component
  

  // This is an autoRemove method on the filter function that
  // when given the new filter value and returns true, the filter
  // will be automatically removed. Normally this is just an undefined
  // check, but here, we want to remove the filter if it's not a number
  


function SearchCourseTable() {
  filterGreaterThan.autoRemove = val => typeof val !== 'number'
  let nav = useNavigate();

  const columns = React.useMemo(
    () => [
      {
        Header: 'Name',
        columns: [
          {
            Header: 'Course Name',
            accessor: 'courseName',
            filter: 'fuzzyText',
          },
          {
            Header: 'Course Num',
            accessor: 'courseNum',
            filter: 'fuzzyText',
          },
          {
            Header: 'Instructor First Name',
            accessor: 'instructorFN',
            filter: 'fuzzyText',
          },
          {
            Header: 'Instructor Last Name',
            accessor: 'instructorLN',
            filter: 'fuzzyText',
          },
          {
            Header: "Semester",
            accessor: "semester",
            Filter: SelectColumnFilter,
            filter: 'includes',
          },
          {
            Header: "Department",
            accessor: "dept",
            Filter: SelectColumnFilter,
            filter: 'includes',
          },
          {
            Header: "Level",
            accessor: "level",
            Filter: SelectColumnFilter,
            filter: 'includes',
          },
          {
            Header: "Overall Rate",
            accessor: "oRate",
            Filter: NumberRangeColumnFilter,
            filter: 'between',
          },
          {
            Header: "Teaching Rate",
            accessor: "tRate",
            Filter: NumberRangeColumnFilter,
            filter: 'between',
          },
          {
            Header: "Hour",
            accessor: "hour",
            Filter: SliderColumnFilter,
            filter: filterGreaterThan,
          },
          {
            Header: "Detail",
            accessor: "detail",                
            
            Cell: ({ cell }) => (
              <Button value={cell.row.values.name} 
                size="sm" onClick = {()=> nav(`${cell.row.id}`)} variant="info">
                Info
              </Button>
            ),
            disableFilters:true
          },
        ],
      },
    ],
    []
  );
    
  
  const [tableData, setTableData] = useState([])
  useEffect(()=> {
    const res = []
    get("course")
    .then(resp => {
    let courseData = resp.data.course;            
    let i, c;
    console.log(courseData)
    console.log(courseData.length)
    for (i = 0; i < courseData.length; i++) {
      c = courseData[i];      
      res.push({
      // "id": c.id, 
      "courseName": c.course_name,
      "courseNum": c.course_number,
      "instructorFN": c.course_instructor_firstname,
      "instructorLN": c.course_instructor_lastname,
      "semester": c.course_semester, 
      "dept": c.course_department,
      "level": c.course_level, 
      "oRate": c.course_overall_rate,
      "tRate": c.course_teaching_rate,
      "hour": c.course_hour,
      "detail": "detail"
      })
    }
    // setX(res.slice(0, 4500))
    setTableData(res) // 4500 之後有一筆會報warning的數據(估計是空值或不符規定的值) 
  })  
  
  },[])
 
  return (    
    <div style={{marginLeft: "260px"}}>
    <Styles>
        <Table columns={columns} data={tableData} />
    </Styles>
    </div>
  )
}

export default SearchCourseTable
