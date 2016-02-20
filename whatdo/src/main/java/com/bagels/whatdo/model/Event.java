package com.bagels.whatdo.model;

/**
 * @author Ari Weiland
 */
public class Event {

    private String name;
    private String url;
    private String cost;
    private String groupSize;
    private String duration;
    private String distance;
    private String description;

    public Event() {
    }

    public Event(String name, String url, String cost, String groupSize, String duration, String distance, String description) {
        this.name = name;
        this.url = url;
        this.description = description;
        this.cost = cost;
        this.groupSize = groupSize;
        this.duration = duration;
        this.distance = distance;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public String getCost() {
        return cost;
    }

    public void setCost(String cost) {
        this.cost = cost;
    }

    public String getGroupSize() {
        return groupSize;
    }

    public void setGroupSize(String groupSize) {
        this.groupSize = groupSize;
    }

    public String getDuration() {
        return duration;
    }

    public void setDuration(String duration) {
        this.duration = duration;
    }

    public String getDistance() {
        return distance;
    }

    public void setDistance(String distance) {
        this.distance = distance;
    }
}
