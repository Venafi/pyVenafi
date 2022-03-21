from pytpp.plugins.properties.response_objects.dataclasses import reports


class Report:
    @staticmethod
    def Column(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return reports.Column(
            stored_name=response_object.get('storedName'),
            nested_table=[Report.NestedTable(t) for t in (response_object.get('nestedTable', []) or [])],
            show_time=response_object.get('showTime'),
            show_date=response_object.get('showDate'),
            name=response_object.get('name'),
            field=response_object.get('field'),
            rank=response_object.get('rank'),
            is_active=response_object.get('isActive'),
            can_sort=response_object.get('canSort'),
            can_be_deactivated=response_object.get('canBeDeactivated'),
            allows_rank_change=response_object.get('allowsRankChange'),
            column_width=response_object.get('columnWidth'),
            type_id=response_object.get('typeId'),
        )

    @staticmethod
    def NestedTable(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return reports.NestedTable(
            type=response_object.get('type'),
            name=response_object.get('name'),
            columns=[Report.Column(c) for c in (response_object.get('columns', []) or [])]
        )
